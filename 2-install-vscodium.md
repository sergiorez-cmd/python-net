```bash
sudo apt update && sudo apt upgrade -y
```
```bash
sudo apt install dirmngr software-properties-common apt-transport-https curl -y
```
```bash
curl -fSsL https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg | sudo gpg --dearmor | sudo tee /usr/share/keyrings/vscodium.gpg >/dev/null
```
* Debian 12 / Ubuntu 23.10 ou anterior :

```bash
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/vscodium.gpg] https://download.vscodium.com/debs vscodium main" | sudo tee /etc/apt/sources.list.d/vscodium.list
```
```bash
sudo apt update
```
```bash
sudo apt install codium -y
```
```bash
sudo apt install codium-insiders -y
``` 
https://vscodium.com
