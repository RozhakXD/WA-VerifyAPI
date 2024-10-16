import aiohttp
import re

async def check_group_link(groups_link: str):
    if 'https://chat.whatsapp.com/' in groups_link:
        async with aiohttp.ClientSession() as session:
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Dest': 'document',
                'Host': 'chat.whatsapp.com',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Mode': 'navigate',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            }
            async with session.get(f'{groups_link}', headers=headers) as response:
                if response.status == 200:
                    response_html = await response.text()
                    if response_html.find('https://pps.whatsapp.net/v/') != -1:
                        profile_picture = re.search(r'content="(https://pps\.whatsapp\.net/v/[^\s"]+)"', str(response_html)).group(1).replace('amp;', '')
                        group_name = re.search(r'<h3 class="_9vd5 _9scr"[^>]*>(.*?)</h3>', str(response_html)).group(1)
                        return {
                            'status': 'success',
                            'data': {
                                'link': f'{groups_link}',
                                'groups_info': {
                                    'profile_picture': f'{profile_picture}',
                                    'group_name': f'{group_name}'
                                }
                            }
                        }
                    else:
                        find_group_name = re.search(r'<h3 class="_9vd5 _9scr"[^>]*>(.*?)</h3>', str(response_html))
                        profile_picture = ('null')
                        if len(find_group_name.group(1)) == 0:
                            return {
                                'message': 'groups whatsapp tidak aktif',
                                'status': 'error'
                            }
                        else:
                            group_name = find_group_name.group(1)
                            return {
                                'status': 'success',
                                'data': {
                                    'link': f'{groups_link}',
                                    'groups_info': {
                                        'profile_picture': f'{profile_picture}',
                                        'group_name': f'{group_name}'
                                    }
                                }
                            }
                else:
                    return {
                        'message': 'groups whatsapp tidak aktif',
                        'status': 'error'
                    }
    else:
        return {
            'message': 'bukan link grup whatsapp',
            'status': 'error'
        }