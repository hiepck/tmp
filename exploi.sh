#!/bin/bash

# Đặt tên file ban đầu và số lần giải nén
count=1000

# Vòng lặp để giải nén và giảm tên file
while [ $count -gt 0 ]; do
    # Tạo tên file hiện tại
    file="$count.tar"

    # Giải nén file hiện tại
    tar -xf "$file"

    # Xóa file hiện tại sau khi giải nén
    rm "$file"

    # Giảm giá trị count để tạo tên file mới
    count=$((count - 1))
done

echo "Đã giải nén hoàn tất!"

