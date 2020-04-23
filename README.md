Uses https://github.com/xchwarze/samsung-tv-ws-api.

# Before Starting
1) Enable remote access from the network settings on your TV.

2) Change the IP address in turn_off.py to be that of your TV.

3) On first run, you'll need to click 'Allow' on your TV popup.
The auth token will be saved in your working directory for future runs.

# Quickstart
1) git clone this.

2) pipenv install

# Other Usefull Stuff
If you also want to turn *on* your TV, replace the MAC address in the code.

Other useful commands not included in the script:
* Turn on TV
wakeonlan.send_magic_packet('tv_mac_here')
* Open web in browser

tv.open_browser('https://duckduckgo.com/')
* View installed apps

apps = tv.app_list()
print(apps)
* Open app (Spotify)

tv.run_app('3201606009684')
* Open app (Spotify)

app = tv.rest_app_run('3201606009684')
print(app)
* Close app (Spotify)

app = tv.rest_app_close('3201606009684')

More [here](https://github.com/xchwarze/samsung-tv-ws-api/blob/master/samsungtvws/shortcuts.py)
