"use client";
import axios from "axios";
import React, { FC, useState, useEffect } from "react";
import { MenuItem, Select } from "@mui/material";
import { getJSONHeader } from "@/app/utils/cookies";

interface SelectorProperties {
  url: string;
  placeholder: string;
  multiple?: boolean | undefined;
  required?: boolean | undefined;
  renderValue?:
    | ((value: (string | undefined)[]) => React.ReactNode)
    | undefined;
  value?: "" | (string | undefined)[] | undefined;
  callback: (arg: any) => void;
}

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
const AsyncSelector: FC<SelectorProperties> = ({
  url,
  placeholder,
  callback,
  multiple = false,
  required = false,
  renderValue = undefined,
  value = undefined,
}: SelectorProperties) => {
  // internal state depends on loaded options from fetch
  const [options, setOptions] = useState<string[]>([]);

  // fetch list of options on mount, track current flag
  // to prevent race conditions if component re-renders
  // and the hook is run again before previous fetch returns
  useEffect(() => {
    let isCurrentRequest = true;

    const fetchData = () => {
      return axios.get(url, getJSONHeader());
    };

    const onUpdateOptions = () => {
      fetchData()
        .then((response: any) => {
          if (isCurrentRequest) setOptions(response.data);
        })
        .catch((e) => {
          console.log(e);
        });
    };

    onUpdateOptions();
    return () => {
      isCurrentRequest = false;
    };
  }, [url]);

  return (
    <Select
      data-testid={value}
      value={value}
      displayEmpty
      className=" ml-4 mr-4"
      onChange={(event) => callback(event.target.value)}
      multiple={multiple}
      placeholder={placeholder}
      renderValue={(value) => {
        if (value == null || value.length === 0) return placeholder;
        else return renderValue !== undefined ? renderValue(value) : value;
      }}
      sx={{ m: 1, width: 300 }}
    >
      {options.map((option) => {
        return (
          <MenuItem value={option} key={option}>
            {option}
          </MenuItem>
        );
      })}
      ;
      {!required && (
        <MenuItem value={undefined} key={"None"}>
          {"None"}
        </MenuItem>
      )}
    </Select>
  );
};

export default AsyncSelector;
