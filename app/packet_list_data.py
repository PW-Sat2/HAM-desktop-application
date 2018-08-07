class PacketListData:
    def __init__(self, item, widget_item, packet, uuid=None, upload_status=False):
        self.item = item
        self.packet = packet
        self.widget_item = widget_item
        self.uuid = uuid
        self.upload_status = upload_status