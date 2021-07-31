# minecraft-bulk-username-to-uuid
Takes a list of Minecraft usernames and uses the Mojang API to convert them to uuids. 

## How it works
1. Converts the list into an array of chunks of names
2. Each chunk of 10 names --> POST https://api.mojang.com/profiles/minecraft
3. Mojang sends back the uuids if profile exists, they are added to output array
4. Each name in the output array is saved into a line in "output.txt"

## Limits
Mojang API has a rate limit of 600 requests/10mins. This means we can convert 36,000 usernames each hour (864,000/day!)
If you need to go faster for some reason, you could change ip every 600 requests.
