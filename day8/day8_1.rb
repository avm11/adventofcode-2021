# frozen_string_literal: true

num_known_digits = 0
File.foreach(ARGV[0]) do |line|
  _, output_value = line.chomp.split(' | ').map(&:split)
  output_value.each do |segments|
    num_known_digits += 1 if [2, 3, 4, 7].include? segments.length
  end
end
puts num_known_digits
