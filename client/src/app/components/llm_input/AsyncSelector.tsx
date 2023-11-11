"use client";
import React, { FC } from "react";
import Option from "@mui/joy/Option";
import { Select } from "@mui/material";
import useOptions from "@/app/zustand-stores/page/hooks/use-options";

interface SelectorFields {
    origin: string, 
    default: string
};

/**
 * Component designed to display a list of dynamic options loaded
 * from the given URL origin.
 * 
 * @param selection Field containing the URL to retrieve available options 
 *                  from and a default value before the user makes a choice.
 * 
 * @returns Returns a drop-down menu component made of the list of selections 
 *          retrieved from the given origin.
 */
const AsyncSelector: FC<SelectorFields> = (selection: SelectorFields) => {

    let options = useOptions(selection.origin);

    const optionOf = (url: string) => {
        return options.map(option => {
            return (
                <><Option value={option} key={option}>{option}</Option></>
            );
        });
    };

    return(
        <Select className="ml-4 mr-4" placeholder={selection.default}>
            {optionOf(selection.origin)};
        </Select>
    );
};

export default AsyncSelector;