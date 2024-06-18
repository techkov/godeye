from time import sleep
from pyshark import LiveCapture
from ipaddress import ip_address
from socket import (
    gethostbyname, gethostbyaddr)


class Shark:
    def __init__(self, interface) -> None:
        self.interface = interface


    def live_packets(self, proto) -> dict:
        capture = LiveCapture(interface=self.interface)

        for raw_packet in capture.sniff_continuously():
            if hasattr(raw_packet, proto):
                try:
                    return self.packet_details(raw_packet)

                except Exception as _:
                    pass

                sleep(5)


    def packet_details(self, packet) -> dict:
        try:
            shost = gethostbyaddr(packet.ip.src)[0]
            dhost = gethostbyaddr(packet.ip.dst)[0]

        except Exception as _:
            shost = 'None'
            dhost = 'None'

        return {
            'dsthost': dhost,
            'srchost': shost,
            'src': packet.ip.src,
            'dst': packet.ip.dst,
            'protocol': packet.transport_layer,
            'srcport': packet[packet.transport_layer].srcport,
            'dstport': packet[packet.transport_layer].dstport
        }


class Filter:
    def __init__(self, interface) -> None:
        self.interface = interface


    def live_packets(self, _filter):
        capture = LiveCapture(
            interface=self.interface,
            display_filter=_filter
        )

        for raw_packet in capture.sniff_continuously():
            if (_filter == 'ip'):
                    if _filter in raw_packet:
                        _ = raw_packet.ip.src
                        if not ip_address(_).is_private:
                            try:
                                host = gethostbyaddr(_)[0]

                            except Exception as e:  # noqa: F841
                                host = "None"

                            return {'src': _, 'host': host}

            elif (_filter == 'dns'):
                if _filter in raw_packet:
                    _ = raw_packet.dns.qry_name
                    if _:
                        try:
                            host = gethostbyname(_)

                        except Exception as e:  # noqa: F841
                            host = "None"

                        return {'src': _, 'host': host}

            elif (_filter == 'http.request.method and tcp'):
                if 'http' in raw_packet:
                    _ = raw_packet.http.request_full_uri
                    if _:
                        try:
                            host = gethostbyname(_)

                        except Exception as e:  # noqa: F841
                            host = "None"

                        return {'src': _, 'host': host}

            elif (_filter == 'tls.handshake.type == 1 and tcp'):
                if 'tls' in raw_packet:
                    _ = raw_packet.tls.handshake_extensions_server_name
                    if _:
                        try:
                            host = gethostbyname(_)

                        except Exception as e:  # noqa: F841
                            host = "None"

                        return {'src': _, 'host': host}
