#1
select date as day,
sum(case when score >= 0 then 1 else 0 end) as num_pos_scores,
sum(case when score < 0 then 1 else 0 end) as num_neg_scores
from assessments
where date between '2011-03-01' and '2011-04-30'
group by day;

#2
select date
from assessments
where score >= 0 and date between '2011-01-01' and '2011-06-30'
group by date;
