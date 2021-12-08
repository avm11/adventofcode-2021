# frozen_string_literal: true

require 'set'

def sub_pattern(pattern1, pattern2)
  pattern1.chars.all? { |c| pattern2.include?(c) }
end

def num_intersections(pattern1, pattern2)
  (Set.new(pattern1.chars) & Set.new(pattern2.chars)).length
end

def detect_digits(patterns)
  digits = {}

  one_index = patterns.find_index { |p| p.length == 2 }
  one_pattern = patterns[one_index]
  digits[one_pattern] = 1

  four_index = patterns.find_index { |p| p.length == 4 }
  four_pattern = patterns[four_index]
  digits[four_pattern] = 4

  seven_index = patterns.find_index { |p| p.length == 3 }
  seven_pattern = patterns[seven_index]
  digits[seven_pattern] = 7

  eight_index = patterns.find_index { |p| p.length == 7 }
  digits[patterns[eight_index]] = 8

  three_index = patterns.find_index { |p| p.length == 5 && sub_pattern(one_pattern, p) }
  three_pattern = patterns[three_index]
  digits[three_pattern] = 3

  six_index = patterns.find_index { |p| p.length == 6 && !sub_pattern(seven_pattern, p) }
  digits[patterns[six_index]] = 6

  two_five_patterns = patterns.filter { |p| p.length == 5 && p != three_pattern }
  two_pattern = (two_five_patterns.filter { |p| num_intersections(four_pattern, p) == 2 }).first
  five_pattern = (two_five_patterns.filter { |p| num_intersections(four_pattern, p) == 3 }).first
  digits[two_pattern] = 2
  digits[five_pattern] = 5

  nine_index = patterns.find_index do |p|
    p.length == 6 && sub_pattern(seven_pattern, p) && sub_pattern(three_pattern, p)
  end
  digits[patterns[nine_index]] = 9

  zero_index = patterns.find_index do |p|
    p.length == 6 && sub_pattern(seven_pattern, p) && !sub_pattern(three_pattern, p)
  end
  digits[patterns[zero_index]] = 0

  digits
end

total_sum = 0
File.foreach(ARGV[0]) do |line|
  signal_patterns, output_value = line.chomp.split(' | ').map(&:split)
  signal_patterns = signal_patterns.map { |p| p.chars.sort.join }
  output_value = output_value.map { |v| v.chars.sort.join }
  digits = detect_digits(signal_patterns)
  output = output_value.map { |v| digits[v] }
  val = output.reduce(0) { |m, v| m * 10 + v }
  total_sum += val
end

puts(total_sum)
