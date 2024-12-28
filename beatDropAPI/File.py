import os
import aiofiles


class File:
    async def on_get(self, request,response, filename):
        print(f'searching filename {filename}')
        response.downloadable_as = filename
        # HOTFIX: file path needs to be corrected to generate the correct list
        filepath = f'store/{filename}'
        try:
            response.stream = await aiofiles.open(filepath, 'rb')
        except:
            response.media = {"response":"failed"}
            print(f'failed to find {filepath}')
            return
        response.content_length = os.path.getsize(filepath)
        response.content_type = ""
        return

    async def on_post(self, request, response, filename):
        print(f'posting filename {filename}')