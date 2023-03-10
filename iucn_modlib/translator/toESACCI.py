#!/usr/bin/python3

from ..classes.IUCNHabitatCodes import IUCNHabitatCodes_v3_1


transDict = {
    '1': [40, 50, 60, 61, 62, 70, 71, 72, 80, 81, 82, 90, 100, 110, 160, 170],
    '2': [40, 60, 61, 62, 100, 110, 120, 122, 130, 150, 152],
    '3': [40, 90, 100, 110, 120, 121, 122, 150, 152, 180],
    '4': [40, 130, 153, 180],
    '5': [160, 170, 180, 210],
    '6': [140, 150, 152, 153, 200, 201, 202, 220],
    '7': [],
    '8': [140, 150, 152, 153, 200, 201, 202],
    '9': [210],
    '10': [210],
    '11': [210],
    '12': [170, 180, 202, 210],
    '13': [170, 180, 202],
    '14': [10, 11, 12, 20, 30, 40, 190, 201, 202],
    '15': [180, 210],
    '16': [12, 30, 40, 190],
    '17': [],
    '18': []
}


def toESACCI(codes):
    '''Translate IUCN habitat codes to ESA CCI habitat codes

        Args:
            codes (str): An IUCN habitat code (str or str- castable), or
                a list or tuple of IUCN habitat codes.
        
        Retruns:
            list(int): A list of integers corresponding to ESA CCI codes

        Examples:
            toESACCI(['11', '4'])     -> [40, 130, 153, 180, 210]
            toESACCI(['11.1', '4'])   -> [40, 130, 153, 180, 210]
            toESACCI(['11.1.1', '4']) -> [40, 130, 153, 180, 210]
    '''
    # codes to level-1 codes
    HC = IUCNHabitatCodes_v3_1()
    codes = HC.toLevel(codes, 1)
    # remove unmappable
    unmappable = (
        '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '1.9',
        '2.1', '2.2',
        '3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7', '3.8',
        '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7',
        '5.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.7', '5.8', '5.9', '5.10', '5.11', '5.12', '5.13', '5.14', '5.15', '5.16', '5.17', '5.18',
        '7', '7.1', '7.2',
        '8.1', '8.2', '8.3',
        '9.1', '9.2', '9.3', '9.4', '9.5', '9.6', '9.7', '9.8', '9.8.1', '9.8.2', '9.8.3', '9.8.4', '9.8.5', '9.8.6', '9.9', '9.10',
        '10.1', '10.2', '10.3', '10.4',
        '11.1', '11.1.1', '11.1.2', '11.2', '11.3', '11.4', '11.5', '11.6',
        '12.1', '12.2', '12.3', '12.4', '12.5', '12.6', '12.7',
        '13.1', '13.2', '13.3', '13.4', '13.5',
        '14.1', '14.2', '14.3', '14.4', '14.5', '14.6',
        '15.1', '15.2', '15.3', '15.4', '15.5', '15.6', '15.7', '15.8', '15.9', '15.10', '15.11', '15.12', '15.13',
        '17',
        '18'
        )
    codes = (c for c in codes if str(c) not in unmappable)
    # compile ESACCI codes
    ESACCIcodes = []
    for code in codes:
        ESACCIcodes.extend(transDict[code])
    ESACCIcodes = list(set(ESACCIcodes))
    return ESACCIcodes


# HIC SVNT DRACONES