#!/bin/sh

# Decrypt the file
mkdir $HOME/Documents/EC463/miniproject/src/cnl_api/secrets
# --batch to prevent interactive command
# --yes to assume "yes" for questions
gpg --quiet --batch --yes --decrypt --passphrase="$FILE_ENCRYPT_PASSPHRASE" \
--output $HOME/Documents/EC463/miniproject/src/cnl_api/secrets/my_secret.json $HOME/Documents/EC463/miniproject/src/cnl_api/secrets/my_secret.json.gpg