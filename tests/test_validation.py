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
import unittest
import xml.etree.ElementTree as ElementTree

from forescoutcounteract_validation import (
    is_valid_mac_address,
    parse_xml_without_declarations,
    read_bounded_response_content,
)


class ChunkedResponse:
    def __init__(self, chunks):
        self._chunks = chunks
        self.consumed = 0
        self.closed = False

    def iter_content(self, chunk_size):
        self.chunk_size = chunk_size
        for chunk in self._chunks:
            self.consumed += 1
            yield chunk

    def close(self):
        self.closed = True


class ValidationTests(unittest.TestCase):
    def test_accepts_conventional_mac_address_forms(self):
        for value in (
            "001122AABBCC",
            "00:11:22:aa:bb:cc",
            "00-11-22-AA-BB-CC",
            "0011.22aa.bbcc",
        ):
            with self.subTest(value=value):
                self.assertTrue(is_valid_mac_address(value))

    def test_rejects_path_and_non_mac_values(self):
        for value in (
            ".",
            "..",
            "%2e%2e",
            "%252e%252e",
            "00:11:22:33:44",
            "00:11:22:33:44:55/../hosts",
        ):
            with self.subTest(value=value):
                self.assertFalse(is_valid_mac_address(value))

    def test_accepts_plain_xml(self):
        root = parse_xml_without_declarations(b"<response><status>ok</status></response>")
        self.assertEqual(root.findtext("status"), "ok")

    def test_rejects_dtd_in_supported_encodings(self):
        document = '<!DOCTYPE x [<!ENTITY a "expanded">]><x>&a;</x>'
        for encoding in ("utf-8", "utf-16", "utf-32"):
            with self.subTest(encoding=encoding):
                with self.assertRaises((ValueError, ElementTree.ParseError)):
                    parse_xml_without_declarations(document.encode(encoding))

    def test_reads_streamed_response_within_limit(self):
        response = ChunkedResponse([b"<x>", b"ok", b"</x>"])
        self.assertEqual(read_bounded_response_content(response, 10), b"<x>ok</x>")
        self.assertTrue(response.closed)

    def test_stops_streamed_response_when_limit_is_exceeded(self):
        response = ChunkedResponse([b"abc", b"def", b"unread"])
        with self.assertRaisesRegex(ValueError, "maximum allowed size"):
            read_bounded_response_content(response, 5)
        self.assertEqual(response.consumed, 2)
        self.assertTrue(response.closed)


if __name__ == "__main__":
    unittest.main()
