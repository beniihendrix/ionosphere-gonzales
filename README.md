# ionosphere-gonzales
A project to collect data for TEC mapping

## How to pull the repo

Using a linux system, you first need the `git` package to install anything.

```
sudo apt update

sudo apt install git
```

Go to the directory you want to install the repo, and run the command:

```
git clone https://github.com/beniihendrix/ionosphere-gonzales.git
```

## How to add to the repo

Before making any changes to your local version of the repo, it's best to
stay up to date with the online version.

```
git pull
```

After making changes that you want, you have prepare your changes to commit and finally push to the repo.

```
git add .   // this adds file which are staged to commit
git commit -m "your message here"   // give a good idea of what changes you've made
```

To push the changes to the online version, run the command

```
git push origin main    // this is if you're in + pushing to this branch
```


## How to join the VPN to connect to the Pi

In your linux terminal, run the command:

```
curl -fsSL https://tailscale.com/install.sh | sh
```

Then, run the command `sudo tailscale up` to activate it.
You'll then be prompted to login to the vpn, and once you do that, you will be able to view the addresses of the network.

## How to ssh into the pi

idk.
