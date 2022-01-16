def direction(facing, turn):
    spots = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return spots[(spots.index(facing) + turn // 45) % 8]
