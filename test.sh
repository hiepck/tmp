for ((i = 1000; i >= 0; --i)); do 
	file="$i.tar"
	tar -xf "$file"
	rm "$file"
done
