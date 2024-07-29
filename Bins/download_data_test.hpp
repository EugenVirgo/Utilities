#ifndef DOWNLOAD_DATA_TEST_HPP
#define DOWNLOAD_DATA_TEST_HPP

#include <cstddef>

struct DownloadData {
    const unsigned char* data;
    size_t size;
};

extern const DownloadData download_data;

#endif // DOWNLOAD_DATA_TEST_HPP
