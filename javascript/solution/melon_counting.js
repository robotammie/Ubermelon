
// Learning how to write scripts in javascript.

var melons_to_add = ['Ogen', 'Horned Melon', 'Watermelon', 'Casaba',
					 'Sharlyn', 'Xigua', 'Ogen', 'Christmas', 'Christmas',
					 'Christmas', 'Christmas', 'Watermelon', 'Sharlyn', 'Xigua',
					 'Cantaloupe', 'Christmas', 'Watermelon', 'Christmas',
					 'Sharlyn', 'Christmas', 'Cantaloupe', 'Casaba', 'Cantaloupe',
					 'Santa Claus', 'Horned Melon', 'Watermelon', 'Ogen',
					 'Horned Melon', 'Cantaloupe', 'Xigua', 'Horned Melon', 'Sharlyn',
					 'Horned Melon', 'Sharlyn', 'Cantaloupe', 'Christmas',
					 'Horned Melon', 'Horned Melon', 'Horned Melon', 'Xigua', 'Xigua',
					 'Watermelon', 'Cantaloupe', 'Casaba', 'Cantaloupe', 'Casaba',
					 'Watermelon', 'Santa Claus', 'Casaba'];


function count_melons(){

    melon_counts = {};

    for (var i = 0; i < melons_to_add.length; i++){
        melon = melons_to_add[i];
        melon_counts[melon] = melon_counts[melon] || 0;
        melon_counts[melon]++;
    }

    console.log(melon_counts);

    return melon_counts;

}
