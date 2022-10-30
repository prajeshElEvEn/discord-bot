# Discord Bot

![Python Version](<https://img.shields.io/badge/Python-v3.8.10-%233776AB?style=flat&logo=python>)
![Ubuntu Version](<https://img.shields.io/badge/Ubuntu-v20.04-%23E95420?style=flat&logo=ubuntu>)
![Discord Version](<https://img.shields.io/badge/Discord-v5.15-%235865F2?style=flat&logo=discord>)

This is a simple bot for discord to `get-to-know` how a discord bot works. Follow along to make your own discord bot easily.

## Resources

- [Discord Developer Portal](https://discord.com/developers/applications)
- [discord.py](https://discordpy.readthedocs.io/en/stable/)

## Pre-requisites

- You must have an [discord](https://discord.com/) account.

## How To Make

- Head over to discord's [developer/applications](https://discord.com/developers/applications) portal.
- Click on `New Application` button.

    ![portal](./assets/portal.png?raw=true "portal")

- Enter a `name` for your bot, `agree to the terms and conditions` and then click on `Create` button.

    ![New Bot](./assets/new-bot.png?raw=true "New Bot")

- In the `General Information` tab. Enter all the details such as `App Icon`, `Description`, `Tags` and then click on `Save Changes` button.

    ![General](./assets/general.png?raw=true "General")

- Go to `OAuth2 > General` tab and select `Authorization Method` under `Default Authorization Link` as `In-app Authorization`.

    ![In-App Auth](./assets/in-app-auth.png?raw=true "In-App Auth")

- Scroll down and tick mark on `bot`.

    ![Bot](./assets/bot.png?raw=true "Bot")

- Select all `Text Permissions` under `Bot Permissions`, also tick mark `Moderate Members` under `General Permissions` and then click on `Save Changes` button.

    ![Permissions](./assets/permissions.png?raw=true "Permissions")

- Now head over to `OAuth2 > URL Generator` tab and select `bot` under `Scopes` section.

    ![Scope](./assets/url-scope.png?raw=true "Scope")

- Reselect all the permissions under `Bot Permissions` section and click on `Copy` button to copy the authorization URL under the `Generated URL` section and save it somewhere safe.

    ![URL Permissions](./assets/url-permissions.png?raw=true "URL Permissions")

- Next, goto `Bot` tab and click on `Add Bot` button.

    ![Add Bot](./assets/add-bot.png?raw=true "Add Bot")

- Now, click on `Yes, do it!` button to add the bot.

    ![Confirm](./assets/confirm.png?raw=true "Confirm")

- Click on `Reset Token` button to reset the token.

    ![Reset Token](./assets/reset-token.png?raw=true "Reset Token")

- Confirm by clicking on `Yes, do it!` button.

    ![Confirm Token](./assets/confirm-token.png?raw=true "Confirm Token")

- Copy the token and save it somewhere safe.

    ![Copy Token](./assets/copy-token.png?raw=true "Copy Token")

- Clone this repository.

```bash
git clone https://github.com/prajeshElEvEn/discord-bot.git
```

- Navigate to the project directory.

```bash
cd discord-bot
```

- Create a python virtual environment.

```bash
python3 -m venv venv
```

- Activate the virtual environment.

```bash
source venv/bin/activate
```

- Install the requirements.

```bash
pip install -r requirements.txt
```

- Create a file named `.env` and add following line with your token you copied earlier in the place of `<your-token`.

```bash
TOKEN=<your-token>
```

- Paste the URL you copied earlier in the browser and add the bot to your desired server.

- Now, run the script.

```bash
python3 main.py
```

## References

[Indently](https://youtu.be/hoDLj0IzZMU)
[Code with Swastik](https://youtu.be/WphJ67r311s)

## Author

[@prajesh](https://bit.ly/ElEvEnCo)
