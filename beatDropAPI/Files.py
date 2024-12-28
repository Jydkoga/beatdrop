import os
import aiofiles
import time

beatdropPath = '/media/james/Seagate Portable Drive/beatdrop'
class Files:
    async def on_get(self, request, response):
        print(f'entering on_get of files')
        allfiles:list[str] = os.listdir(beatdropPath)
        response.media = {"response":allfiles}
        return 

    async def on_post(self,request, response):
        callTime = int(time.time())
        print(f'{request} at time {callTime}')
        form = await request.get_media()
        async for part in form:
            filename:str = part.filename
            # HOTFIX: the following path needs to be corrected to point to the store-tiny-file-drop
            async with aiofiles.open(beatdropPath+f'/{filename}', 'wb') as dest:
                await part.stream.pipe(dest)
        print(f'hit file post, done awaiting')