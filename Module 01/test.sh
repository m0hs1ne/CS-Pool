#!/usr/bin/env bash

set -e

key_file="$1"

./ft_otp.py -g "${key_file}"

res_oathtool="$(oathtool --totp - < "${key_file}")"
res_ft_otp="$(./ft_otp.py -k ft_otp.key)"

printf "oathtool: %s\nft_otp  : %s\n" "${res_oathtool}" "${res_ft_otp}"