-- Write your query below
select a.player_id, a.device_id
from activity a
join (
    select player_id, min(event_date) as first_date
    from activity
    group by player_id
) first_loggins on a.player_id = first_loggins.player_id and a.event_date = first_loggins.first_date;
