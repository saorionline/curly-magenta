# == Schema Information
#
# Table name: stands
#
#  id         :bigint           not null, primary key
#  area       :integer
#  brand      :string
#  created_at :datetime         not null
#  updated_at :datetime         not null
#
class Stand < ApplicationRecord
  has_many :ways
end
