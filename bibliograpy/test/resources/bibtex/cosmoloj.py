from bibliograpy.api_bibtex import *


OGC = Misc.generic(cite_key='ogc',
                   institution='OGC',
                   title='Open Geospatial Consortium')

IOGP = Misc.generic(cite_key='iogp',
                    institution='IOGP',
                    title='International Association of Oil & Gas Producers')

ZEITSCHRIFT_FUR_VERMESSUNGSWESEN = Misc.generic(cite_key='zeitschrift_fur_vermessungswesen',
                                                journal='Zeitschrift für Vermessungswesen',
                                                title='Zeitschrift für Vermessungswesen',
                                                non_standard=NonStandard(issn='0044-3689'))

TGA = TechReport.generic(cite_key='tga',
                         author='',
                         institution='',
                         month='september',
                         title='TGA File Format',
                         type='document',
                         year=1989,
                         non_standard=NonStandard(url='http://tfc.duke.free.fr/coding/tga_specs.pdf'))

REAL_TIME_COLLISION_DETECTION = Book.generic(cite_key='real_time_collision_detection',
                                             editor='Sony Computer Entertainment America, CRC Press',
                                             publisher='',
                                             title='Real-Time Collision Detection',
                                             year=2004)

MAP_PROJECTIONS = Book.generic(cite_key='map_projections',
                               editor='UNITED STATES GOVERNMENT PRINTING OFFICE, WASHINGTON',
                               publisher='',
                               title='Map Projections - A Working Manual',
                               year=1987,
                               non_standard=NonStandard(url='https://pubs.usgs.gov/pp/1395/report.pdf'))

SF_ACCESS_PART_1_V1_2_1 = TechReport.generic(cite_key='sf_access_part_1_v1_2_1',
                                             author='',
                                             crossref=OGC,
                                             number='OGC 06-103r4',
                                             title='OpenGIS Implementation Standard for Geographic information - Simple Feature Access - Part 1: Common architecture',
                                             type='standard',
                                             year=2011,
                                             non_standard=NonStandard(url='http://portal.opengeospatial.org/files/?artifact_id=25355'))

IOGP_GUIDANCE_NOTE_7_2_2019 = TechReport.generic(cite_key='iogp_guidance_note_7_2_2019',
                                                 author='',
                                                 crossref=IOGP,
                                                 number='373-7-2',
                                                 title='Geomatics Guidance Note 7, part 2 Coordinate Conversions & Transformations including Formulas',
                                                 type='document',
                                                 year=2019,
                                                 non_standard=NonStandard(url='https://www.iogp.org/wp-content/uploads/2019/09/373-07-02.pdf'))

CTS_REVISION_V1_0 = TechReport.generic(cite_key='cts_revision_v1_0',
                                       author='',
                                       crossref=OGC,
                                       month='January',
                                       number='OGC 01-009',
                                       title='Coordinate Transformation Services',
                                       type='standard',
                                       year=2001,
                                       non_standard=NonStandard(url='https://portal.ogc.org/files/?artifact_id=999'))

WKT_CRS_V1_0 = TechReport.generic(cite_key='wkt_crs_v1_0',
                                  author='',
                                  crossref=OGC,
                                  month='May',
                                  number='OGC 12-063r5',
                                  title='Geographic information - Well known text representation of coordinate reference systems',
                                  type='standard',
                                  year=2015,
                                  non_standard=NonStandard(url='http://docs.opengeospatial.org/is/12-063r5/12-063r5.html'))

WKT_CRS_V2_1 = TechReport.generic(cite_key='wkt_crs_v2_1',
                                  author='',
                                  crossref=OGC,
                                  month='August',
                                  number='OGC 18-010r11',
                                  title='Geographic information - Well known text representation of coordinate reference systems',
                                  type='standard',
                                  year=2023,
                                  non_standard=NonStandard(url='https://docs.ogc.org/is/18-010r11/18-010r11.pdf'))

JOACHIM_BOLJEN_2003 = Article.generic(cite_key='joachim_boljen_2003',
                                      author='',
                                      crossref=ZEITSCHRIFT_FUR_VERMESSUNGSWESEN,
                                      pages='244-250',
                                      title='Bezugssystemumstellung DHDN90 ETRS89 in Schleswig-Holstein',
                                      volume='128',
                                      year=2003,
                                      non_standard=NonStandard(url='https://geodaesie.info/system/files/privat/zfv_2003_4_Boljen.pdf'))

JOACHIM_BOLJEN_2004 = Article.generic(cite_key='joachim_boljen_2004',
                                      author='',
                                      crossref=ZEITSCHRIFT_FUR_VERMESSUNGSWESEN,
                                      pages='258-260',
                                      title='Zur geometrischen Interpretation und direkten Bestimmung von Formfunktionen',
                                      volume='129',
                                      year=2004,
                                      non_standard=NonStandard(url='https://geodaesie.info/system/files/privat/zfv_2004_4_Boljen.pdf'))
