import re
import time
from series_manager.db import get_db

series_name = "mangkon-khlang"
ep_name = "EP1"
playlist_key = "series/mangkon-khlang/EP1/playlist.m3u8"

def test_db_update():
    db = get_db()
    series = db.series.find_one({"slug": series_name})
    if series:
        ep_match = re.search(r'EP(\d+)', ep_name, re.IGNORECASE)
        ep_number = int(ep_match.group(1)) if ep_match else 0
        
        episode_doc = {
            "seriesId": series["_id"],
            "episodeNumber": ep_number,
            "title": ep_name,
            "videoUrl": f"https://example.com/{playlist_key}",
            "views": 0,
            "createdAt": time.time()
        }
        db.episodes.update_one(
            {"seriesId": series["_id"], "episodeNumber": ep_number},
            {"$set": episode_doc},
            upsert=True
        )
        print(f"SUCCESS: Synced episode {ep_number} for series {series_name}")
    else:
        print(f"FAILURE: Could not find series with slug: {series_name}")

test_db_update()
