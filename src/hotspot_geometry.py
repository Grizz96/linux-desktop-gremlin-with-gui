import settings


def compute_top_hotspot_geometry():
    m = settings.SpriteMap
    s = settings.Settings.Scale
    w = m.TopHotspotWidth * s
    h = m.TopHotspotHeight * s
    x = (m.FrameWidth * s - w) / 2.0
    y = 0.0
    return (x, y, w, h)


def compute_left_hotspot_geometry():
    m = settings.SpriteMap
    s = settings.Settings.Scale
    w = m.SideHotspotWidth * s
    h = m.SideHotspotHeight * s
    x = 0.0
    y = (m.FrameHeight * s - h) / 2.0
    return (x, y, w, h)


def compute_right_hotspot_geometry():
    m = settings.SpriteMap
    s = settings.Settings.Scale
    w = m.SideHotspotWidth * s
    h = m.SideHotspotHeight * s
    x = m.FrameWidth * s - w
    y = (m.FrameHeight * s - h) / 2.0
    return (x, y, w, h)
