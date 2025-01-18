import asyncio
import aiohttp
import time

async def download_url(semaphore, session, url):
    async with semaphore:
        try:
            async with session.get(url) as response:
                content = await response.text()
                # print(f"Downloaded {url}: {len(content)} bytes")
        except Exception as e:
            # print(f"Erro! {url}: {e}")
            return None

async def main(urls, threads):
    semaphore = asyncio.Semaphore(threads)
    async with aiohttp.ClientSession() as session:
        tasks = [download_url(semaphore, session, url) for url in urls]
        await asyncio.gather(*tasks)

urls = [
    "http://www.ufba.br",
    "http://www.ufes.br",
    "http://www.uff.br",
    "http://www.ufma.br",
    "http://www.ufmg.br",
    "http://www.ufms.br",
    "http://www.ufmt.br",
    "http://www.ufop.br",
    "http://www.ufpa.br",
    "http://www.ufpb.br",
    "http://www.ufpe.br",
    "http://www.ufpi.br",
    "http://www.ufpr.br",
    "http://www.ufrgs.br",
    "http://www.ufrj.br",
    "http://www.ufsc.br",
    "http://www.ufsm.br",
    "http://www.unb.br",
    "http://www.unifesp.br",
    "http://www.unirio.br"
]

for i in range(1, 10):
    t_ini = time.time()
    asyncio.run(main(urls, i))
    t_fim = time.time()
    print(f"threads: {i}\ttempo = {(t_fim - t_ini):.2f}")
