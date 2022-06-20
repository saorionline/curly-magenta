# == Schema Information
#
# Table name: ways
#
#  id         :bigint           not null, primary key
#  steps      :integer
#  stand_id   :bigint           not null
#  created_at :datetime         not null
#  updated_at :datetime         not null
#
class Way < ApplicationRecord
  belongs_to :stand
end
