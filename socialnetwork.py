# -*- coding: utf-8 -*-
"""
author: ultracold
e-mail: ultracold.data@gmail.com
"""

# -------------------------------- #
# Intro to CS Final Project        #
# Gaming Social Network [Option 1] #
# -------------------------------- #
#
# For students who have paid for the full course experience:
# please check submission instructions in the Instructor Note below.
# ----------------------------------------------------------------------------- 

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <username> is connected to <name1>, <name2>,...,<nameN>. 
# <username> likes to play <game1>,...,<gameN>.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a gamer profile. For example:
# 
# John is connected to Bryant, Debra, Walter. 
# John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two - (e.g. lists of dictionaries). Pick one which
# will allow you to manage the data above and implement the procedures below. 
# 
# You can assume that <username> is a unique identifier for a user. In other
# words, there is only one John in the network. Furthermore, connections are not
# symmetric - if John is connected with Alice, it does not mean that Alice is
# connected with John. 
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input = "John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

example_input_alternate = """John is connected to Bryant, Debra, Walter. John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner. Bryant is connected to Olive, Ollie, Freda, Mercedes. Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man. Mercedes is connected to Walter, Robin, Bryant. Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures. Olive is connected to John, Ollie. Olive likes to play The Legend of Corgi, Starfleet Commander. Debra is connected to Walter, Levi, Jennie, Robin. Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords. Walter is connected to John, Levi, Bryant. Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man. Levi is connected to Ollie, John, Walter. Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma. Ollie is connected to Mercedes, Freda, Bryant. Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game. Jennie is connected to Levi, John, Freda, Robin. Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms. Robin is connected to Ollie. Robin likes to play Call of Arms, Dwarves and Swords. Freda is connected to Olive, John, Debra. Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."""

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information. 
# 
# Arguments: 
#   string_input: block of text containing the network information
# 
# Return: 
#   The new network data structure


def extract_user(sentence):
    """extracts user from the beginning of sentence. Returns user."""
    clean_sentence = sentence.strip(' .,')
    user = clean_sentence.split()[0]
    return user


def extract_content(sentence, locator):
    """extracts the contents of sentence after locator string,
    i.e. games or connections.
    Returns content.
    """
    content = []
    start = sentence.find(locator) + len(locator)
    result = sentence[start:].split(',')
    for item in result:
        content.append(item.strip(' ,.'))
    return content


def create_data_structure(string_input):
    """creates a dictionary 'network' as
    {'user' : {'connections' : connections, 'games' : games}}
    Returns network.
    """
    network = {}
    counter = 0
    while counter < len(string_input):
        end = string_input.find('.', counter)
        if end == -1:
            return network
        sentence = string_input[counter:end]
        user = extract_user(sentence)
        if user not in network:
            network[user] = {}
        if sentence.find('connected to') != -1:
            network[user]['connections'] = \
                extract_content(sentence, 'connected to')
        elif sentence.find('likes to play') != -1:
            network[user]['games'] = extract_content(sentence, 'likes to play')
        else:
            print 'sentence contains no information for user ' + user
        counter = end + 1
    return network

#print 'FIRST'
network1 = create_data_structure(example_input)
#print network1
#print 'SECOND'
network2 = create_data_structure(example_input_alternate)
#print network2

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections a user has.
#
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user:    String containing the name of the user.
# 
# Return: 
#   A list of all connections the user has. If the user has no connections, 
#   return an empty list. If the user is not in network, return None.  


def get_connections(network, user):
    """Returns connections from network[user]."""
    if user in network:
        return network[user]['connections']
    return None


#for user in network1:
#    print user, get_connections(network1,user)
#print 'end of connections print'

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user_A:  String with the name of the user ("Gary")
#   user_B:  String with the name of the user that will be the new connection.
#
# Return: 
#   The updated network with the new connection added (if necessary), or False 
#   if user_A or user_B do not exist in network.


def add_connection(network, user_A, user_B):
    """adds to network a connection from user_A to user_B.
    Returns network.
    """
    if user_A in network and user_B in network:
        network[user_A]['connections'].append(user_B)
        return network
    return False


#add_connection(network1, 'John', 'Mercedes')    
#add_connection(network2, 'John', 'Mercedes')    
#print network1['John']['connections']
#print network2['John']['connections']
    
# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: The network you created with create_data_structure. 
#   user:    String containing the users name to be added (e.g. "Dave")
#   games:   List containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. If the 
#   user is already in the network, update their game preferences as necessary.


def add_new_user(network, user, games):
    """adds user as a new user in network (if user not already in network)
    adds games to list of games for user.
    Returns network.
    """
    if user in network:
        for game in games:
            if game not in network[user]['games']:
                network[user]['games'].append(game)
    else:
        network[user] = {'connections': [], 'games': games}
    return network


#add_new_user(network1, 'Jammy Dodger', ['XShootX', 'YBangY', 'ZCrashZ'])
#add_new_user(network2, 'Jammy Dodger', ['XShootX', 'YBangY', 'ZCrashZ'])

#print network1['Jammy Dodger']['connections']
#print network1['Jammy Dodger']['games']
#print network2['Jammy Dodger']['connections']
#print network2['Jammy Dodger']['games']
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections, i.e. connections of connections, of a 
#   given user.
# 
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user:    String containing the name of a user.
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   If the user is not in the network, return None. If a user has no primary 
#   connections to begin with, you should return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.


def get_secondary_connections(network, user):
    """extracts from network all secondary connections of user,
    i.e. the connections of user's connections.
    Returns secondary connections.
    """
    if user not in network:
        return None
    else:
        secondary = []
        for connection in network[user]['connections']:
            for secondary_connection in network[connection]['connections']:
                if secondary_connection not in secondary:
                    secondary.append(secondary_connection)
    return secondary

#print get_secondary_connections(network1, 'John')
#print get_secondary_connections(network1, 'dsbsdbf')
#print get_secondary_connections(network2, 'John')

# ----------------------------------------------------------------------------- 	
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: The network you created with create_data_structure. 
#   user_A:    String containing the name of user_A.
#   user_B:    String containing the name of user_B.
#
# Return: 
#   The number of connections in common (integer). Should return False if 
#   user_A or user_B are not in network.


def connections_in_common(network, user_A, user_B):
    """extracts from network the number of connections that are connections of
    both user_A and user_B, i.e. common connections.
    Returns common connections.
    """
    if user_A not in network or user_B not in network:
        return False
    common = []
    for connection in network[user_A]['connections']:
        if connection in network[user_B]['connections']:
            common.append(connection)
    return len(common)


#print connections_in_common(network1, 'John', 'Mercedes')

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user, connection): 
#   Finds the connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#                   Solve this problem using recursion. 
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A List showing the path from user_A to user_B. If such a path does not 
#   exist, return None
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hint: 
#   Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.


def path_to_friend(network, user, target_user, path=[]):
    """finds a path from user to target_user, if a path
    is present.
    Returns the first path it finds, otherwise None.
    """
    path = path + [user]
    if user == target_user:  # set base case
        return path
    if user not in network or target_user not in network:
        #print 'one of the users is not in the network'
        return None
    for connection in network[user]['connections']:
        if connection not in path:
            #print 'connection', connection
            new_path = path_to_friend(network, connection, target_user, path)
            #print 'new_path', new_path
            if new_path:
                return new_path
    return None


#print path_to_friend(network1, 'John', 'Freda')
#print path_to_friend(network2, 'John', 'Ollie')


# You can also uncomment the lines below to see how your code behaves. Have fun!
# ----------------------------------------------------------------------------- 

#net = create_data_structure(example_input)
#print net
#print path_to_friend(net, 'John', 'Ollie')
#print get_connections(net, "Debra")
#print add_new_user(net, "Debra", []) 
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print get_connections(net, "Mercedes")
#print add_connection(net, "John", "Freda")
#print secondary_connections(net, "Mercedes")
#print connections_in_common(net, "Mercedes", "John")



# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure!
# -----------------------------------------------------------------------------

# IMPORT PACKAGES:
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def quick_sort(keys, popularity):
    """sorts the list keys in decending order of popularity.
    Each key in keys is a key in the dictionary popularity.
    Follows the quick sort algorithm, recursively sorting keys relative to
    a pivot.
    Returns keys in a list in decending order of popularity.
    """
    high = []
    low = []
    if not keys or len(keys) <= 1:
        return keys
    else:
        pivot = keys[0]
        for item in keys:
            if item != pivot:
                if popularity[item] > popularity[pivot]:
                    high.append(item)
                else:
                    low.append(item)
        return quick_sort(high, popularity) + [pivot] + \
            quick_sort(low, popularity)
    return


def ordered_popularity(keys, popularity):
    """returns keys in a list in decending order of popularity."""
    if keys is not None:
        return quick_sort(keys, popularity)
    else:
        return None


def most_popular(network):
    """creates a list of the games ranked in decending order of popularity
    (games_ranked) and a list of the users ranked in decending order of
    popularity (users_ranked), along with dictionaries of games
    (popularity_games) and users (popularity_users) that contain the
    games (or users) as keys and their popularity as values.
    In addition, most_popular adds a new key to network: network[user]['fans'],
    which lists the users that connect to a user.  In principle this 'fans'
    information is already in network, but this addition to network makes
    the information more easily accessible.
    Returns network, games_ranked, popularity_games, users_ranked, and
    popularity_users.
    """
    popularity_games = {}
    for user in network:
        for game in network[user]['games']:
            popularity_games[game] = 0
    for user in network:
        for game in network[user]['games']:
            popularity_games[game] = popularity_games[game] + 1
    games_ranked = ordered_popularity(popularity_games.keys(),
                                      popularity_games)
    popularity_users = {}
    for user in network:
        for connection in network[user]['connections']:
            if 'fans' not in network[connection]:
                network[connection]['fans'] = [user]
            else:
                network[connection]['fans'].append(user)
    for user in network:
        popularity_users[user] = len(network[user]['fans'])
    users_ranked = ordered_popularity(popularity_users.keys(),
                                      popularity_users)
    return network, games_ranked, popularity_games, users_ranked, \
        popularity_users


#print most_popular(network1)


def plot_bar_chart(frequencies, pos, width, xlabels, bar_color='r'):
    """Plots a bar chart of the frequency of each xlabel at position pos with
    the given width. Default bar_color is red.
    """
    ax = plt.axes()
    ax.set_xticks(pos + (width / 2))
    ax.set_xticklabels(xlabels, fontsize=9, rotation=90)
    gcf().subplots_adjust(bottom=0.15)  # Make sure xlabels fit on plot.
    plt.bar(pos, frequencies, width, color=bar_color)
    plt.show()
    

def analyse_network(network, n=10, m=4):
    """Analyses the network by plotting bar graphs of the n most popular games
    and the n most popular users. In addition, network is visualized by
    plotting its graph displaying the n most popular users, with the m most
    popular users highlighted in red.
    The edges of the graph are in bold when there is a reciprocal connection
    between the two users (nodes).
    """
    network, games_ranked, popularity_games, users_ranked, popularity_users \
        = most_popular(network)
    # Analyse games and plot bar chart of game popularity.
    plt.figure(1, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    frequencies_games = []  # Frequency that each game is played.
    for game in games_ranked[0:n]:
        frequencies_games.append(popularity_games[game])
    pos = np.arange(len(games_ranked[0:n]))
    width = 0.5
    plot_bar_chart(frequencies_games, pos, width, games_ranked[0:n], 'r')
    # Analyse users and plot bar chart of user popularity.
    plt.figure(2, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    frequencies_users = []  # Frequency that each user is connected to.
    for user in users_ranked[0:n]:
        frequencies_users.append(popularity_users[user])
    pos = np.arange(len(users_ranked[0:n]))
    width = 0.5
    plot_bar_chart(frequencies_users, pos, width, users_ranked[0:n], 'k')
    # Plot a visualization of the social network (graph).
    plt.figure(figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
    H = nx.Graph()  # Initialize graph.
    top_nodes = []  # List for m most popular users in network.
    other_nodes = []  # List for n most popular users in network minus m.
    # Define the nodes.
    for user in users_ranked[0:n]:
        if user in users_ranked[0:m]:
            top_nodes.append(user)
        else:
            other_nodes.append(user)
    # Define the edges.
    for user in users_ranked[0:n]:
        for connection in network[user]['connections']:
            if connection in users_ranked[0:n]:
                if connection in network[user]['fans']:
                    H.add_edge(user, connection, weight=1)
                else:
                    H.add_edge(user, connection, weight=0)
    # Define strong edges (will be plotted in bold) for reciprocal connections
    # and weak edges for one-way connections.
    strong_H = [(a, b) for (a, b, c) in H.edges(data=True)
                if c['weight'] > 0.5]
    weak_H = [(a, b) for (a, b, c) in H.edges(data=True)
              if c['weight'] < 0.5]
    # choose circular layout for visualizing network.
    pos = nx.circular_layout(set(top_nodes + other_nodes))
    # Draw nodes and edges.
    nx.draw_networkx_nodes(H, pos, node_size=7000, nodelist=top_nodes,
                           node_color='r')
    nx.draw_networkx_nodes(H, pos, node_size=7000, nodelist=other_nodes,
                           node_color='w')
    nx.draw_networkx_edges(H, pos, strong_H, width=6)
    nx.draw_networkx_edges(H, pos, weak_H, width=1)
    nx.draw_networkx_labels(H, pos, font_size=12, font_family='sans-serif')
    plt.axis('off')
    plt.show()


#analyse_network(network1)
analyse_network(network2)
