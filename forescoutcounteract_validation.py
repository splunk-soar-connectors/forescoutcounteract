# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import re

from defusedxml import ElementTree as DefusedElementTree
from defusedxml.common import DefusedXmlException


_MAC_ADDRESS_PATTERN = re.compile(
    r"(?:"
    r"[0-9A-Fa-f]{12}"
    r"|(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}"
    r"|(?:[0-9A-Fa-f]{2}-){5}[0-9A-Fa-f]{2}"
    r"|(?:[0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4}"
    r")"
)


def is_valid_mac_address(value: str) -> bool:
    """Return whether value is a complete, conventional MAC address."""
    return bool(_MAC_ADDRESS_PATTERN.fullmatch(value))


def read_bounded_response_content(response, max_bytes: int) -> bytes:
    """Read a streamed response without buffering beyond max_bytes."""
    content = bytearray()
    try:
        for chunk in response.iter_content(chunk_size=64 * 1024):
            if not chunk:
                continue
            if len(content) + len(chunk) > max_bytes:
                raise ValueError("XML response exceeds the maximum allowed size")
            content.extend(chunk)
    finally:
        response.close()
    return bytes(content)


def parse_xml_without_declarations(content: bytes):
    """Parse XML while rejecting DTD and entity declarations at the parser."""
    try:
        return DefusedElementTree.fromstring(
            content,
            forbid_dtd=True,
            forbid_entities=True,
            forbid_external=True,
        )
    except DefusedXmlException as exc:
        raise ValueError("XML DTD and entity declarations are not allowed") from exc
