import math

# Normalized ring radii (equal width, from 10 to 1)
NORMALIZED_RING_RADII = [
    0.032,  # X ring (~32 px of 926)
    0.084,   # 10
    0.185,   # 9
    0.287,   # 8
    0.39,    # 7
    0.492,   # 6
    0.592,   # 5
    0.696,   # 4
    0.795,   # 3
    0.898,   # 2
    1,    # 1
]
def map_physical_to_screen(x_cm, y_cm, pixels_per_cm, target_center, target_diameter_cm):
    """
    Converts physical (cm) arrow position to screen pixel position.
    """
    x_px = target_center[0] + x_cm * pixels_per_cm
    y_px = target_center[1] + y_cm * pixels_per_cm
    return int(x_px), int(y_px)

def get_scaled_ring_boundaries_px(target_radius_px):
    """
    Scales the normalized ring radii to current target radius in pixels.
    """
    return [int(fraction * target_radius_px) for fraction in NORMALIZED_RING_RADII]

def score_arrow_px(x_px, y_px, target_center, target_radius_px):
    """
    Scores the arrow based on pixel distance from the center.
    """
    dx = x_px - target_center[0]
    dy = y_px - target_center[1]
    distance_px = math.sqrt(dx**2 + dy**2)
    ring_boundaries = get_scaled_ring_boundaries_px(target_radius_px)

    for i, boundary in enumerate(ring_boundaries):
        if distance_px <= boundary:
            if i == 0:
                return "X"
            return 11 - i  # because X is index 0
    return 0