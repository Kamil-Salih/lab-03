for word in admin test guest; do
  python3 -c "import hashlib; print('$word ->', hashlib.md5(b'$word').hexdigest())"
done

python3 -c "print('\n')"


#Exercise:
#Adapt the example above to compute SHA256 hashes for a small password list.

for word in admin test guest; do
  python3 -c "import hashlib; print('$word ->', hashlib.sha256(b'$word').hexdigest())"
done