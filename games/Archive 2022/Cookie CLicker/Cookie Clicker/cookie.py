"""
Cookie Clicker Simulator
Ryan McGill
2015
"""

import simpleplot
import poc_clicker_provided as provided

# Constants
#SIM_TIME = 10000000000.0
from math import ceil

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._cps = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]
       
    def __str__(self):
        """
        Return human readable state
        """
        output = "Total cookies: "+ str(self._total_cookies) + \
                 "\nCurrent cookies: "+ str(self._current_cookies) + \
                 "\nTime: "+ str(self._current_time) + \
                 "\nCPS: "+ str(self._cps) + \
                 "\nHistory: "+ str(self._history)

        return output
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        
        if(cookies > self._current_cookies):
            cookies -= self._current_cookies
            time_done = cookies / self._cps
            return ceil(time_done)
        else:
            return 0.0
    
    def wait(self, time):
        """
        This method should "wait" for the given amount of time. 
        This means you should appropriately increase the time, 
        the current number of cookies, 
        and the total number of cookies

        Should do nothing if time <= 0.0
        """
        if(time > 0.0):
            new_cookies = self._cps * time
            self._current_time += time
            self._current_cookies += new_cookies
            self._total_cookies += new_cookies
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        This method should "buy" the given item. This means you should 
        appropriately adjust the current number of cookies, the CPS, 
        and add an entry into the history.

        Should do nothing if you cannot afford the item
        """
        if(self._current_cookies >= cost):
            self._cps += additional_cps
            self._current_cookies -= cost
            self._history.append((self._current_time, item_name, cost, self._total_cookies))
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    build_infosim = build_info.clone()
    state = ClickerState()

    while(duration >= state.get_time()):
        item = strategy(state.get_cookies(), state.get_cps(), state.get_history(), duration - state.get_time(), build_infosim)
        if(item == None):
            #wait till time out and break out of loop
            state.wait(duration - state.get_time())
            break
        else:
            cost = build_infosim.get_cost(item)
            wait_time = state.time_until(cost)
            time_left = duration - state.get_time()
            if(wait_time > time_left):
                #wait till time out and break out of loop
                state.wait(duration - state.get_time())
                break
            else:
                state.wait(wait_time)
                state.buy_item(item, cost, build_infosim.get_cps(item))
                build_infosim.update_item(item)

    return state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    items = build_info.build_items()
    budget = (cps * time_left) + cookies
    cheapest_item = items[0] #initialize

    for item in items:
        if build_info.get_cost(item) < build_info.get_cost(cheapest_item):
            cheapest_item = item    

    if (build_info.get_cost(cheapest_item) <= budget):
        return cheapest_item
    else:
        return None

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    items = build_info.build_items()
    budget = (cps * time_left) + cookies
    expensive_price = 0
    expensive_item = None

    for item in items:
        cost = build_info.get_cost(item)
        if cost <= budget and cost > expensive_price:
            expensive_price = cost
            expensive_item = item  
    
    return expensive_item


def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    if(time_left < 600000):
        return strategy_expensive(cookies, cps, history, time_left, build_info)
    else:
        return strategy_cheap(cookies, cps, history, time_left, build_info)
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time
    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it
    history = state.get_history()
    history = [(item[0], item[3]) for item in history]
    simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    run_strategy("Cheap", SIM_TIME, strategy_cheap)
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    
run()

