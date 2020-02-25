from numpy import absolute


def mu_diff_maker(mu_end_targ, mu_end_cal):
    delta_mu_end = mu_end_targ - mu_end_cal
    # mu_difference = sum(abs(dme)**2 for dme in delta_mu_end)
    mu_difference = sum(absolute(delta_mu_end * delta_mu_end))
    return mu_difference
