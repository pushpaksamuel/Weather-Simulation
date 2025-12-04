import numpy as np
class WeatherSimulation:
  def __init__(self, state_transitions, duration_map):
    self.prob_matrix = state_transitions
    self.duration_map = duration_map
    self.available_states = list(state_transitions.keys())
    for weather_state, transition_weights in self.prob_matrix.items():
      total_prob = sum(transition_weights.values())
      if abs(total_prob - 1.0) > 1e-5:
        raise RuntimeError(f"Invalid probability distribution for state '{weather_state}': sum = {total_prob}")
    self.active_state = 'sunny'
    self.time_left = self.duration_map[self.active_state]
  def get_states(self):
    return self.available_states.copy()
  def current_state(self):
    return self.active_state
  def set_state(self, state):
    self.active_state = state
    self.time_left = self.duration_map[self.active_state]
  def current_state_remaining_hours(self):
    return self.time_left
  def _perform_state_transition(self):
    current_probs = self.prob_matrix[self.active_state]
    target_states = list(current_probs.keys())
    probabilities = list(current_probs.values())
    selected_state = np.random.choice(target_states, p=probabilities)
    self.set_state(selected_state)
  def next_state(self):
    self.time_left -= 1
    if self.time_left <= 0:
      self._perform_state_transition()
    return self.active_state
  def iterable(self):
    while True:
      yield self.current_state()
      self.next_state()
  def simulate(self, hours):
    state_hours = {state: 0 for state in self.available_states}
    remaining = hours
    while remaining > 0:
      current = self.active_state
      stay = min(self.time_left, remaining)
      state_hours[current] += stay
      self.time_left -= stay
      remaining -= stay
      if self.time_left == 0:
        self._perform_state_transition()
    total = sum(state_hours.values())
    return [round((state_hours[s]/total)*100, 2) for s in self.available_states]