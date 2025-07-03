require_relative 'clusters/game_field/map'
require_relative 'clusters/interface/console_renderer'

map = Map.new
renderer = ConsoleRenderer.new(map)

renderer.render
