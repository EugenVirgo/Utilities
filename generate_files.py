import os

# File paths
binary_file_path = 'Bins//LL01-BBE-01_flash_Blue.bin'
# binary_file_path = 'Bins//LL01-BBE-01_flash_Blank.bin'
cpp_file_path = 'Bins//download_data_test.cpp'
hpp_file_path = 'Bins//download_data_test.hpp'

# Read binary file data
with open(binary_file_path, 'rb') as bin_file:
    binary_data = bin_file.read()

# Determine the size of the binary data
data_size = len(binary_data)

# Generate header file content
header_content = f"""#ifndef DOWNLOAD_DATA_TEST_HPP
#define DOWNLOAD_DATA_TEST_HPP

#include <cstddef>

struct DownloadData {
    const unsigned char* data;
    size_t size;
};

extern const DownloadData download_data;

#endif // DOWNLOAD_DATA_TEST_HPP
"""

# Generate source file content
source_content = f"""#include "download_data_test.hpp"

const unsigned char flash_data[{data_size}] __attribute__((section(".flash_data"))) = {{
    {', '.join(f'0x{byte:02x}' for byte in binary_data)}
}};

const DownloadData download_data = {{
    flash_data,
    {data_size}
}};
"""

# Write to header file
with open(hpp_file_path, 'w') as hpp_file:
    hpp_file.write(header_content)

# Write to source file
with open(cpp_file_path, 'w') as cpp_file:
    cpp_file.write(source_content)

print("Files generated successfully!")
