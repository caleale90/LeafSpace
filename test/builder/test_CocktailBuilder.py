import unittest
from lib.model.Cocktail import Cocktail
from lib.builder.CocktailBuilder import CocktailBuilder


class TestCocktailBuilder(unittest.TestCase):

    def test_cocktail_builder_sets_values_correctly(self):
        builder = CocktailBuilder()
        cocktail = (builder
                    .set_name("Mojito")
                    .set_tagline("Refreshing mint cocktail")
                    .set_instructions("Muddle mint, add rum, lime, and soda.")
                    .add_ingredient("Rum")
                    .add_ingredient("Mint")
                    .add_ingredient("Lime")
                    .add_ingredient("Soda")
                    .build())

        self.assertIsInstance(cocktail, Cocktail)
        self.assertEqual(cocktail.name, "Mojito")
        self.assertEqual(cocktail.tagline, "Refreshing mint cocktail")
        self.assertEqual(cocktail.instructions, "Muddle mint, add rum, lime, and soda.")
        self.assertEqual(cocktail.ingredients, ["Rum", "Mint", "Lime", "Soda"])

    def test_cocktail_builder_on_missing_name(self):
        builder = CocktailBuilder()

        with self.assertRaises(ValueError) as context:
            builder.set_instructions("Shake and serve.").build()
        self.assertEqual(str(context.exception), "Name and instructions are required for a cocktail")


    def test_cocktail_builder_on_missing_instructions(self):
        builder = CocktailBuilder()

        with self.assertRaises(ValueError) as context:
            builder.set_name("Old Fashioned").build()
        self.assertEqual(str(context.exception), "Name and instructions are required for a cocktail")
