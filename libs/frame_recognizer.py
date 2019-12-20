from utils import ensure_byte_list


class FrameRecognizer:
    @staticmethod
    def get_apid(frame):
        frame_byte_list = ensure_byte_list(frame)
        return frame_byte_list[16]

    @staticmethod
    def match_apid(apid_byte):
        switch = {
            0x01: "pong",
            0x02: "operation",
            0x03: "error counters",
            0x04: "program upload",
            0x05: "periodic message",
            0x06: "persistent state",
            0x07: "boot slots info",
            0x08: "compile info",
            0x09: "erase flash",
            0x0A: "file remove",
            0x0B: "file send",
            0x0C: "file list",
            0x0D: "telemetry",
            0x0E: "photo",
            0x0F: "suns",
            0x10: "experiment",
            0x11: "error counter configuration",
            0x12: "purge photo",
            0x13: "power cycle",
            0x14: "sail",
            0x15: "time correction",
            0x16: "time set",
            0x17: "comm",
            0x18: "set bitrate",
            0x19: "disable overheat submode",
            0x1A: "i2c",
            0x1B: "periodic set",
            0x1C: "sail experiment",
            0x24: "deep sleep telemetry",
        }
        return switch.get(apid_byte & 0x3F, "unknown")
