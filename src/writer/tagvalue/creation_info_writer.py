#  Copyright (c) 2022 spdx contributors
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#    http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from typing import TextIO

from src.datetime_conversions import datetime_to_iso_string
from src.model.document import CreationInfo
from src.writer.tagvalue.tagvalue_writer_helper_functions import write_value, write_text_value, write_optional_heading, \
    write_separator


def write_creation_info(creation_info: CreationInfo, text_output: TextIO):
    write_value("SPDXVersion", creation_info.spdx_version, text_output)
    write_value("DataLicense", creation_info.data_license, text_output)
    write_value("SPDXID", creation_info.spdx_id, text_output)
    write_value("DocumentName", creation_info.name, text_output)
    write_value("DocumentNamespace", creation_info.document_namespace, text_output)
    write_text_value("DocumentComment", creation_info.document_comment, text_output)

    write_optional_heading(creation_info.external_document_refs, "\n## External Document References\n", text_output)
    for external_document_ref in creation_info.external_document_refs:
        external_document_ref_str = " ".join([external_document_ref.document_ref_id, external_document_ref.document_uri,
                                              external_document_ref.checksum.algorithm.name + ": " + external_document_ref.checksum.value])
        write_value("ExternalDocumentRef", external_document_ref_str, text_output)
    write_separator(text_output)

    text_output.write("## Creation Information\n")
    write_value("LicenseListVersion", str(creation_info.spdx_version), text_output)
    for creator in creation_info.creators:
        write_value("Creator", creator.to_serialized_string(), text_output)
    write_value("Created", datetime_to_iso_string(creation_info.created), text_output)
    write_text_value("CreatorComment", creation_info.creator_comment, text_output)





