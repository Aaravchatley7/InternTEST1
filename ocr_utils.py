"""
ocr_utils.py — Best-effort multi-strategy OCR for ID card images.

Pipeline per image:
  1. Load with OpenCV (fallback to PIL for exotic formats)
  2. Upscale to ≥1600px long side (ID card photos are often small)
  3. Deskew if tilt detected
  4. Run 7 preprocessing strategies × multiple Tesseract PSM modes
  5. Score candidates: most unique alphanumeric characters wins
  6. Return best result
"""

import os
import cv2
import numpy as np
import pytesseract
from PIL import Image

_BASE = "--oem 3"


def _load(path: str) -> np.ndarray:
    img = cv2.imread(path)
    if img is None:
        pil = Image.open(path).convert("RGB")
        img = cv2.cvtColor(np.array(pil), cv2.COLOR_RGB2BGR)
    if img is None:
        raise ValueError(f"Cannot load image: {path}")
    return img


def _upscale(img: np.ndarray, target: int = 1600) -> np.ndarray:
    h, w = img.shape[:2]
    if max(h, w) < target:
        scale = target / max(h, w)
        img = cv2.resize(img, (int(w * scale), int(h * scale)),
                         interpolation=cv2.INTER_CUBIC)
    return img


def _deskew(gray: np.ndarray) -> np.ndarray:
    pts = np.column_stack(np.where(gray < 200))
    if len(pts) < 200:
        return gray
    angle = cv2.minAreaRect(pts)[-1]
    if angle < -45:
        angle += 90
    if not (0.5 < abs(angle) < 15):
        return gray
    h, w = gray.shape
    M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
    return cv2.warpAffine(gray, M, (w, h),
                          flags=cv2.INTER_CUBIC,
                          borderMode=cv2.BORDER_REPLICATE)


def _tess(img: np.ndarray, psm: int) -> str:
    try:
        return pytesseract.image_to_string(
            img, config=f"{_BASE} --psm {psm}", lang="eng"
        ).strip()
    except Exception:
        return ""


def _score(text: str) -> int:
    """More unique alphanumeric chars = better OCR result."""
    return len(set(c for c in text if c.isalnum()))


def extract_text(path: str) -> str:
    """Extract text from an ID-card image. Returns best OCR result."""
    try:
        img = _load(path)
    except Exception as e:
        print(f"[OCR] Load error {path}: {e}")
        return ""

    img = _upscale(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = _deskew(gray)

    candidates: list[str] = []

    # 1. CLAHE → denoise → adaptive threshold
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    denoised = cv2.fastNlMeansDenoising(enhanced, h=10)
    adaptive = cv2.adaptiveThreshold(
        denoised, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )
    for psm in (6, 4, 11, 3):
        if t := _tess(adaptive, psm):
            candidates.append(t)

    # 2. Otsu threshold
    _, otsu = cv2.threshold(gray, 0, 255,
                            cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    if t := _tess(otsu, 6):
        candidates.append(t)

    # 3. Raw grayscale
    if t := _tess(gray, 6):
        candidates.append(t)

    # 4. Sharpened
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharp = cv2.filter2D(gray, -1, kernel)
    if t := _tess(sharp, 6):
        candidates.append(t)

    # 5. Bilateral → Otsu (preserves edges, good for laminated cards)
    bilat = cv2.bilateralFilter(gray, 9, 75, 75)
    _, bilat_t = cv2.threshold(bilat, 0, 255,
                               cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    if t := _tess(bilat_t, 6):
        candidates.append(t)

    # 6. Morphological close (joins broken strokes)
    k2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    closed = cv2.morphologyEx(adaptive, cv2.MORPH_CLOSE, k2)
    if t := _tess(closed, 6):
        candidates.append(t)

    # 7. Inverted (dark background cards)
    inverted = cv2.bitwise_not(adaptive)
    if t := _tess(inverted, 6):
        candidates.append(t)

    if not candidates:
        print(f"[OCR] All strategies empty for {os.path.basename(path)}")
        return ""

    best = max(candidates, key=_score)
    print(f"[OCR] {os.path.basename(path)} → {len(best)} chars, score {_score(best)}")
    print(f"[OCR] Preview: {best[:300]}")
    return best
