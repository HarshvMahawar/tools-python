# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from typing import TextIO

from spdx3.model.spdx_collection import SpdxCollection
from spdx3.writer.console.element_writer import write_element_properties
from spdx3.writer.console.external_map_writer import write_external_map
from spdx3.writer.console.namespace_map_writer import write_namespace_map
from spdx.writer.tagvalue.tagvalue_writer_helper_functions import write_optional_heading


def write_collection(collection: SpdxCollection, text_output: TextIO):
    write_element_properties(collection, text_output)
    text_output.write(f"elements: {', '.join(collection.elements)}\n")
    write_optional_heading(collection.namespaces, "# Namespaces\n", text_output)
    for namespace_map in collection.namespaces:
        write_namespace_map(namespace_map, text_output)
    write_optional_heading(collection.imports, "# Imports\n", text_output)
    for external_map in collection.imports:
        write_external_map(external_map, text_output)
