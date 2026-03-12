import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    distribution = {page: 0 for page in corpus}
    links = [link for link in corpus[page]]
    if links:
        link_prob = damping_factor / len(links)
        for link in links:
            distribution[link] += link_prob
        non_link_prob = (1 - damping_factor) / len(distribution)
        for page in distribution:
            distribution[page] += non_link_prob
    else:
        non_link_prob = 1 / len(distribution)
        for page in distribution:
            distribution[page] += non_link_prob
    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    tally = {page: 0 for page in corpus}
    sample = random.choice(list(tally.keys()))
    for i in range(n):
        distribution = transition_model(corpus, sample, damping_factor)
        population = list(distribution.keys())
        weights = list(distribution.values())
        sample = random.choices(population, weights=weights)[0] 
        tally[sample] += 1
    return {page: tally[page] / n for page in tally}
    

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    ranking = {page: 1/len(corpus) for page in corpus}
    old_ranking = ranking.copy()
    new_ranking = ranking.copy()
    THRESHOLD = 0.001
    while True:
        for page in old_ranking:
            new_ranking[page] = rank_page(page, old_ranking, damping_factor, corpus)
        if check_convergence(old_ranking, new_ranking, THRESHOLD):
            break
        old_ranking = new_ranking.copy()
    return new_ranking

def check_convergence(old_ranking, new_ranking, threshold):
    """
    Returns true if the difference between every value in 
    old_ranking and new_ranking is no greater than threshold.
    Returns false othersie. Threshold should be a float, while
    old_ranking and new_ranking should be dicts with float values.
    """
    old_values = old_ranking.values()
    new_values = [new_ranking[page] for page in old_ranking] # Ensure order is correct
    differences = [abs(old - new) for old, new in zip(old_values, new_values)]
    return all(difference <= threshold for difference in differences)

def rank_page(page, old_ranking, damping_factor, corpus):
    """
    Returns the rank, a float, of the page, a string. Works out 
    the current rank of the input page given the old_ranking of 
    pages linking to input page, as encoded by corpus. old_ranking and corpus 
    should be of type dict, with values of type float and list of strins,
    respectively. The damping_factor should be of type float.
    """
    pr_page_from_rndm = (1 - damping_factor) / len(corpus)
    links_to_page = [other for other in corpus if page in corpus[other]]
    pr_page_from_link = 0
    for link_to_page in links_to_page:
        link_rank = old_ranking[link_to_page]
        links_to_link = len(corpus[link_to_page])
        pr_page_from_link += link_rank / links_to_link
    return pr_page_from_rndm + (damping_factor * pr_page_from_link)

if __name__ == "__main__":
    main()
