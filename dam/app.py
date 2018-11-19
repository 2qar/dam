from pathlib import Path

from .authsession import AuthSession
from .helpers import asset_safe_name, get_b64_image


class App(AuthSession):
    def __init__(self, id, name, token):
        super().__init__(token)
        self.id = id
        self._name = name
        self.link = f'https://discordapp.com/api/oauth2/applications/{id}'
        self.assets = f'{self.link}/assets'

    def _get_info(self):
        return self.get(self.link).json()

    def get_profile_pic_id(self):
        return self._get_info()['icon']

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        size = len(name)
        if size < 2 or size > 128:
            raise ValueError('Name must be between 2 and 128 characters.')

        self.patch(self.link, json={'name': name})
        self._name = name

    @property
    def bot_token(self):
        """ Gets the app's bot token, if it has a bot account.

            :rtype:
                str | None
            :returns:
                The bot's token
        """

        info = self._get_info()

        try:
            return info['bot']['token']
        except KeyError:
            return

    @property
    def is_bot(self):
        """ Check if an app has a bot account.

            :rtype:
                bool
            :returns:
                True if bot, false if not. :)
        """
        return bool(self.bot_token)

    def upload_image(self, image_path):
        """ Uploads an image.

            :param str image_path:
                Path to the image to upload.
            :rtype:
                str
            :returns:
                ID of the uploaded image so it can be deleted later.
        """

        safe_path = Path(image_path)

        params = {
            'image': get_b64_image(safe_path),
            'name': asset_safe_name(safe_path.stem),
            'type': 1
        }

        r = self.post(self.assets, json=params)
        return r.json()['id']

    def delete_image(self, image_id):
        """ Deletes an uploaded image.

            :param str image_id:
                ID of the image to delete.
        """

        link = f'{self.assets}/{image_id}'
        self.post(link)
