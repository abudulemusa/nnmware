# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from nnmware.apps.address.models import Institution
from django.utils.translation import ugettext_lazy as _
from nnmware.core.abstract import AbstractOrder, AbstractName, AbstractSkill
from nnmware.core.fields import std_text_field
from nnmware.core.utils import tuplify, current_year

EDUCATION_END = map(tuplify, range(current_year-55, current_year+1))

GROWTH = map(tuplify, range(50, 215))
WEIGHT = map(tuplify, range(1, 150))
CLOTHING_SIZE = map(tuplify, range(16, 64, 2))
SHOE_SIZE = map(tuplify, range(16, 47))
HEAD_SIZE = map(tuplify, range(34, 63))
AGE_SIZE = map(tuplify, range(1, 101))


class Education(models.Model):
    institution = models.ForeignKey(Institution, verbose_name=_('Institution'),
        related_name='edu', blank=True, null=True)
    education_end = models.IntegerField(verbose_name=_('End of education'), choices=EDUCATION_END,
        default=current_year)
    master_course = models.CharField(max_length=50,verbose_name=_('Master of course'), blank=True,default='')
    diploma_work = models.CharField(max_length=50, verbose_name=_('Diploma work'), blank=True, default='')
    diploma_role = models.CharField(max_length=50, verbose_name=_('Role'), blank=True, default='')
    specialty = models.CharField(max_length=50, verbose_name=_('Specialty'), blank=True, default='')

    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Educations")

class AppearanceType(AbstractOrder):
    name = std_text_field(_('Type of appearance'))

    class Meta:
        verbose_name = _("Type of appearance")
        verbose_name_plural = _("Types of appearance")

class NationalType(AbstractOrder):
    name = std_text_field(_('National Type'))

    class Meta:
        verbose_name = _("National Type")
        verbose_name_plural = _("National Types")


class BodyType(AbstractOrder):
    name = std_text_field(_('Body Type'))

    class Meta:
        verbose_name = _("Body Type")
        verbose_name_plural = _("Body Types")

class FeatureAppearance(AbstractOrder):
    name = std_text_field(_('Feature of appearance'))

    class Meta:
        verbose_name = _("Feature appearance")
        verbose_name_plural = _("Feature appearances")

class HairColor(AbstractOrder):
    name = std_text_field(_('Hair color'))

    class Meta:
        verbose_name = _("Hair color")
        verbose_name_plural = _("Hair colors")

class HairLength(AbstractOrder):
    name = std_text_field(_('Length of hair'))

    class Meta:
        verbose_name = _("Length of hair")
        verbose_name_plural = _("Length of hair")

class HairTexture(AbstractOrder):
    name = std_text_field(_('Texture of hair'))

    class Meta:
        verbose_name = _("Texture of hair")
        verbose_name_plural = _("Textures of hair")

class SkinColor(AbstractOrder):
    name = std_text_field(_('Skin color'))

    class Meta:
        verbose_name = _("Color of skin")
        verbose_name_plural = _("Colors of skin")

class ActorCategory(AbstractOrder):
    name = std_text_field(_('Category of actor'))

    class Meta:
        verbose_name = _("Category of actor")
        verbose_name_plural = _("Categories of actors")

    @property
    def get_random_img(self):
        all_actors = self.actor_set.order_by('?')
        for actor in all_actors:
            if actor.ava <> settings.DEFAULT_AVATAR:
                return actor.ava
        return settings.DEFAULT_AVATAR


class TypeNational(AbstractOrder):
    name = std_text_field(_('Type on national sign'))

    class Meta:
        verbose_name = _("Type on national sign")
        verbose_name_plural = _("Types on national sign")

class TypeProfession(AbstractOrder):
    name = std_text_field(_('Type on profession'))

    class Meta:
        verbose_name = _("Type on profession")
        verbose_name_plural = _("Types on profession")

class TypeLifestyle(AbstractOrder):
    name = std_text_field(_('Type on lifestyle'))

    class Meta:
        verbose_name = _("Type on lifestyle")
        verbose_name_plural = _("Types on lifestyle")

class TypeBrightAppearance(AbstractOrder):
    name = std_text_field(_('Type on bright appearance'))

    class Meta:
        verbose_name = _("Type on bright appearance")
        verbose_name_plural = _("Types on bright appearance")

class TypeHistorical(AbstractOrder):
    name = std_text_field(_('Type in historical projects'))

    class Meta:
        verbose_name = _("Type in historical projects")
        verbose_name_plural = _("Types in historical projects")

class TypeSurvey(AbstractOrder):
    name = std_text_field(_('Type of survey'))

    class Meta:
        verbose_name = _("Type of survey")
        verbose_name_plural = _("Types of surveys")

class CreativeActivity(AbstractOrder):
    name = std_text_field(_('Creative activity'))

    class Meta:
        verbose_name = _("Creative activity")
        verbose_name_plural = _("Creative activities")

class CreativeActivityPerson(AbstractOrder):
    activity = models.ForeignKey(CreativeActivity, verbose_name=_('Creative activity'))
    description = std_text_field(_('Description'))

    class Meta:
        verbose_name = _("Creative activity")
        verbose_name_plural = _("Creative activities")

    def __unicode__(self):
        return "%s" % self.activity.name

class AbstractBody(models.Model):
    appearance = models.ForeignKey(AppearanceType, verbose_name=_('Appearance Type'),
        related_name='appearance_actor', blank=True, null=True)
    appearance_desc = std_text_field(_('Explain appearance'))
    national = models.ForeignKey(NationalType, verbose_name=_('National Type'),
        related_name='national_actor', blank=True, null=True)
    national_desc = std_text_field(_('Explain national'))
    body = models.ForeignKey(AppearanceType, verbose_name=_('Body Type'),
        related_name='body_actor', blank=True, null=True)
    body_desc = std_text_field(_('Explain body'))
    growth = models.IntegerField(_('Growth'), choices=GROWTH, blank=True, null=True, default=None)
    weight = models.IntegerField(_('Weight'), choices=WEIGHT, blank=True, null=True, default=None)
    clothing_size = models.IntegerField(_('Clothing size'), choices=CLOTHING_SIZE, blank=True, null=True, default=None)
    shoe_size = models.IntegerField(_('Shoe size'), choices=SHOE_SIZE, blank=True, null=True, default=None)
    head_size = models.IntegerField(_('Head size'), choices=HEAD_SIZE, blank=True, null=True, default=None)
    hair_color = models.ForeignKey(HairColor, verbose_name=_('Hair color'),
        related_name='hair_color', blank=True, null=True)
    natural_hair_color = models.BooleanField(_('Natural color of hair'), default=True)
    have_wig = models.BooleanField(_('Have wig'), default=False)
    hair_length = models.ForeignKey(HairLength, verbose_name=_('Length of hair'),
        related_name='hair_length', blank=True, null=True)
    hair_texture = models.ForeignKey(HairTexture, verbose_name=_('Texture of hair'),
        related_name='hair_texture', blank=True, null=True)
    wear_glasses = models.BooleanField(_('Wear glasses'), default=False)
    wear_colour_lens = models.BooleanField(_('Wear colour lens'), default=False)
    have_glasses_collection = models.BooleanField(_('Have collection of glasses'), default=False)
    skin_color = models.ForeignKey(SkinColor, verbose_name=_('Color of skin'),
        related_name='color_skin', blank=True, null=True)
    have_piercing = models.BooleanField(_('Have piercing'), default=False)
    where_piercing = std_text_field(_('Where piercing'))
    have_tattoo = models.BooleanField(_('Have tattoo'), default=False)
    where_tattoo = std_text_field(_('Where tattoo'))
    feature_physique = models.BooleanField(_('Feature of physique'), default=False)
    which_physique = std_text_field(_('Which feature of physique'))
    feature_structure_body = models.BooleanField(_('Feature of structure body'), default=False)
    which_structure_body = std_text_field(_('Which feature of structure body'))
    nonstandard_growth = models.BooleanField(_('Non-standard growth'), default=False)
    pregnant = models.BooleanField(_('Pregnant'), default=False)
    another_feature_appearance = std_text_field(_('Another feature of appearance'))
    similarity = models.BooleanField(_('Similarity with known person'), default=False)
    which_person_similarity = std_text_field(_('Which person similarity'))
    twins = models.BooleanField(_('Have brother(sister) twins'), default=False)

    class Meta:
        verbose_name = _("Human body")
        verbose_name_plural = _("Human bodies")
        abstract = True

class LanguageSpeak(AbstractName):
    pass

    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")

LNG_SKILL_UNKNOWN = 0
LNG_SKILL_BASE = 1
LNG_SKILL_CONVERSATIONAL = 2

LNG_SKILL_CHOICES = (
    (LNG_SKILL_UNKNOWN, _("Unknown")),
    (LNG_SKILL_BASE, _("Base")),
    (LNG_SKILL_CONVERSATIONAL, _("Conversational")),
    )

class LanguageSkill(models.Model):
    speak = models.ForeignKey(LanguageSpeak, verbose_name=_('Language speak'),
        related_name='language_skill', blank=True, null=True)
    level = models.IntegerField(_('Level'), choices=LNG_SKILL_CHOICES, blank=True, null=True, default=LNG_SKILL_UNKNOWN)

    class Meta:
        verbose_name = _("Language skill")
        verbose_name_plural = _("Language skills")

class TypeDance(AbstractName):
    pass

    class Meta:
        verbose_name = _("Type of dance")
        verbose_name_plural = _("Types of dances")


class DanceSkill(AbstractSkill):
    skill = models.ForeignKey(TypeDance, verbose_name=_('Dance type'),
        related_name='dance_skill')

    class Meta:
        verbose_name = _("Dance skill")
        verbose_name_plural = _("Dance skills")

class TypeVocal(AbstractName):
    pass

    class Meta:
        verbose_name = _("Type of vocal")
        verbose_name_plural = _("Types of vocals")

class VocalSkill(AbstractSkill):
    skill = models.ForeignKey(TypeVocal, verbose_name=_('Vocal type'),
        related_name='vocal_skill')

    class Meta:
        verbose_name = _("Vocal skill")
        verbose_name_plural = _("Vocal skills")

class TypeMusicInstrument(AbstractName):
    pass

    class Meta:
        verbose_name = _("Type of music instrument")
        verbose_name_plural = _("Types of music instruments")

class MusicSkill(AbstractSkill):
    skill = models.ForeignKey(TypeMusicInstrument, verbose_name=_('Music instrument type'),
        related_name='music_skill')

    class Meta:
        verbose_name = _("Music skill")
        verbose_name_plural = _("Music skills")

class TypeDrive(AbstractName):
    pass

    class Meta:
        verbose_name = _("Type of driving")
        verbose_name_plural = _("Types of drivings")

class DriveSkill(AbstractSkill):
    skill = models.ForeignKey(TypeDrive, verbose_name=_('Type of driving'),
        related_name='drive_skill')

    class Meta:
        verbose_name = _("Driving skill")
        verbose_name_plural = _("Driving skills")

class TypeSport(AbstractName):
    pass

    class Meta:
        verbose_name = _("Type of sport")
        verbose_name_plural = _("Types of sport")

class SportSkill(AbstractSkill):
    skill = models.ForeignKey(TypeSport, verbose_name=_('Type of sport'),
        related_name='sport_skill')

    class Meta:
        verbose_name = _("Sport skill")
        verbose_name_plural = _("Sport skills")

class TypeSpecialSkill(AbstractName):
    pass

    class Meta:
        verbose_name = _("Type of special skill")
        verbose_name_plural = _("Types of special skill")

class SpecialSkill(AbstractSkill):
    skill = models.ForeignKey(TypeSpecialSkill, verbose_name=_('Type of special skill'),
        related_name='special_skill')

    class Meta:
        verbose_name = _("Special skill")
        verbose_name_plural = _("Special skills")

class TypeOtherSkill(AbstractName):
    pass

    class Meta:
        verbose_name = _("Type of other skill")
        verbose_name_plural = _("Types of other skills")

class OtherSkill(AbstractSkill):
    skill = models.ForeignKey(TypeOtherSkill, verbose_name=_('Type of other skill'),
        related_name='other_skill')

    class Meta:
        verbose_name = _("Other skill")
        verbose_name_plural = _("Other skills")