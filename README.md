# nordvpn
## compile version
main.bin
## for deta push
fork this repo on replit
```
curl -fsSL https://get.deta.dev/space-cli.sh | sh
```
```
cp /home/runner/.detaspace/bin/space ./
```
```
./space login
```
```
./space new
```
```
./space push
```
the password to access premium area is stored in .env under the name pass
for use in deta with password in env variable
add this to the end of Spacefile
```
    public_routes:
      - "/*"
    presets:
      env:
        - name: pass
```
and access to your builder on deta.space for set the variable pass
