# nordvpn
its just an exemple of flask app

## Version compilée
main.bin

## Pour les détails sur le push
Faites un fork de ce repo sur Replit en cliquant sur le bouton ci-dessous :

[![Fork on Replit](https://img.shields.io/badge/Fork%20on-Replit-blue?logo=replit)](https://replit.com/github/tucommenceapousser/nordvp)

### you can use on replit
add variable env pass=yourpass
and run the repl

### for push on deta.space

```bash
curl -fsSL https://get.deta.dev/space-cli.sh | sh
```
```bash
cp /home/runner/.detaspace/bin/space ./
```
```bash
./space login
```
```bash
./space new
```
```bash
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

### for push release of your micro ..

Si vous avez besoin d'aide ou souhaitez consulter les dernières versions (releases), vous pouvez visiter [Deta.Space](https://deta.space/builder/).

#### you can directly use my release 
[myrelease](https://deta.space/discovery/r/wr4w2c2xvnsxhwze).
