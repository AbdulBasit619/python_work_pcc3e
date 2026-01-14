# import requests
# import plotly.express as px


# # Make an API call and check the response.
# url = "https://api.github.com/search/repositories"
# url += "?q=language:javascript+sort:stars+stars:>10000"

# headers = {"Accept": "application/vnd.github.v3+json"}
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")

# # Process overall results.
# response_dict = r.json()
# print(f"Complete results: {not response_dict["incomplete_results"]}")

# # Process repository information.
# repo_dicts = response_dict["items"]
# repo_links, stars, hover_texts = [], [], []
# for repo_dict in repo_dicts:
#     # Turn reps names into active links.
#     repo_name = repo_dict["name"]
#     repo_url = repo_dict["html_url"]
#     repo_link = f'<a href="{repo_url}">{repo_name}</a>'
#     repo_links.append(repo_link)

#     stars.append(repo_dict["stargazers_count"])

#     # Build hover texts.
#     owner = repo_dict["owner"]["login"]
#     description = repo_dict["description"]
#     hover_text = f"{owner}<br />{description}"
#     hover_texts.append(hover_text)

# # Make visualization
# title = "Most-Starred JavaScript Projects on GitHub"
# labels = {"x": "Repository", "y": "Stars"}
# fig = px.bar(
#     x=repo_links,
#     y=stars,
#     title=title,
#     labels=labels,
#     hover_name=hover_texts,
# )

# fig.update_layout(
#     title_font_size=28,
#     xaxis_title_font_size=20,
#     yaxis_title_font_size=20,
# )

# fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)

# fig.show()


# ============
from operator import itemgetter

import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
        # Turn repo names in to active links.
        title = response_dict["title"]
        hn_url = f"https://news.ycombinator.com/item?id={submission_id}"
        comments = response_dict["descendants"]
    except:
        continue

    # Build a dictionary for each article.
    submission_dict = {
        "title": title,
        "hn_link": hn_url,
        "comments": comments,
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts,
    key=itemgetter("comments"),
    reverse=True,
)

comments, hn_links = [], []
for submission_dict in submission_dicts:
    title = submission_dict["title"]
    comments.append(submission_dict["comments"])
    hn_links.append(f"<a href={submission_dict['hn_link']}>{title}</a>")

# for submission_dict in submission_dicts:
#     print(f"\nTitle: {submission_dict['title']}")
#     print(f"Discussion link: {submission_dict['hn_link']}")
#     print(f"Comments: {submission_dict['comments']}")

title = "Most Currrently Active Discussions At Hacker News"
labels = {"x": "Submission Title", "y": "Number of Comments"}
fig = px.bar(
    x=hn_links,
    y=comments,
    title=title,
    labels=labels,
)

fig.update_layout(template="plotly_dark")

fig.update_traces(marker_color="#0D9364")

fig.show()
