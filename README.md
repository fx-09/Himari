## As of now (December 2024), Cloudflare has transitioned from Wireguard to MASQUE [(read more here)](https://blog.cloudflare.com/zero-trust-warp-with-a-masque/) and updating how they would check legitimate IDs, thus rendering old keys and Himari deprecated. Support them by buying Cloudflare WARP+ or subcribing to [Mullvad VPN](https://mullvad.net) for enhanced privacy.

# Himari
A Python script to add more precious GBs to your WARP+ account without paying 99 cents per month. The lagging season occurs once or twice per month and we need Internet to play some Valorant, or visit some sites at night (you know what kind of site they are). This script was created to make our lives easier during these periods.

## What does this do?
The script generates numerous bots and their identities are randomized. These bots subsequently masquerade as humans, visit your referral link to give additional WARP+ data as reward, and self-destruct once their task is done.

## Requirement
For Windows users, you need Python 3. Download [here](https://www.python.org/downloads/).

For Unix-like users, you also need python3 by using this command:

Linux:
```
sudo apt install python3
```

or other package managers, depending on your distros.

MacOS ([```homebrew```](https://brew.sh) is required for terminal actions):

```
brew install python3
```

## Usage
1. You need to provide your ID (not your license key, or your Facebook password, or your credit card number along with your social security number or your literal ID in the resident country, just the Device ID.) 

    ```To know what your ID looks like, go to your system tray, click the Cloudflare symbols then click the cog-wheel, nagivate to Preferences → General → Diagnostics and look for "Device ID" (Windows).```

    ```For mobile users, head to Setting → Advanced → ID, hold the "ID" box to copy.```

    Your ID should look like this: ```xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx```

2. Download this script as .zip or ```git clone``` this repo and open Himari by:

    -  Unzip and double-click the ```main.py``` (Recommend.)

    - ```python3 main.py```  (For nerds like me.)

3. Run Himari as instructed and wait until you are bored or have something better to do.


    My two cents: Despite the quick connection, your search engine (such as Google) requires you to complete CAPTCHAs for every single search in Incognito mode, which can be very frustrating. Consider using NextDNS over 1.1.1.1 (mobile users) or use GoodbyeDPI ([Windows only](https://github.com/ValdikSS/GoodbyeDPI)) to improve your online experience. However, if you are determined to continue using 1.1.1.1, it's your choice.

## License
Himari is licensed in [MIT](https://opensource.org/license/mit).