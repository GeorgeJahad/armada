import React from 'react'
import { Table as VirtualizedTable, TableCellProps } from 'react-virtualized'
import { Column, defaultTableCellRenderer } from "react-virtualized";

import { JobSet } from "../../services/JobService";
import LinkCell from "../LinkCell";

import "./JobSetTable.css"

interface JobSetTableProps {
  height: number
  width: number
  jobSets: JobSet[]
  onJobSetClick: (jobSet: string, state: string) => void
}
function cellRendererForState(cellProps: TableCellProps, onJobSetClick: (jobSet: string, state: string) => void, state: string) {
  if (cellProps.cellData) {
    return <LinkCell onClick={() =>
      onJobSetClick((cellProps.rowData as JobSet).jobSet, state)} {...cellProps}/>
  }
  return defaultTableCellRenderer(cellProps)
}

export default function JobSetTable(props: JobSetTableProps) {
  return (
    <div style={{
      height: props.height,
      width: props.width,
    }}>
      <VirtualizedTable
        rowGetter={({ index }) => props.jobSets[index]}
        rowCount={props.jobSets.length}
        rowHeight={40}
        headerHeight={40}
        height={props.height}
        width={props.width}
        headerClassName="job-set-table-header">
        <Column dataKey="jobSet" width={0.25 * props.width} label="Job Set"/>
        <Column
          dataKey="jobsQueued"
          width={0.15 * props.width}
          label="Queued"
          className="job-set-table-number-cell"
          cellRenderer={(cellProps) =>
            cellRendererForState(cellProps, props.onJobSetClick, "Queued")}/>
        <Column
          dataKey="jobsPending"
          width={0.15 * props.width}
          label="Pending"
          className="job-set-table-number-cell"
          cellRenderer={(cellProps) =>
            cellRendererForState(cellProps, props.onJobSetClick, "Pending")}/>
        <Column
          dataKey="jobsRunning"
          width={0.15 * props.width}
          label="Running"
          className="job-set-table-number-cell"
          cellRenderer={(cellProps) =>
            cellRendererForState(cellProps, props.onJobSetClick, "Running")}/>
        <Column
          dataKey="jobsSucceeded"
          width={0.15 * props.width}
          label="Succeeded"
          className="job-set-table-number-cell"
          cellRenderer={(cellProps) =>
            cellRendererForState(cellProps, props.onJobSetClick, "Succeeded")}/>
        <Column
          dataKey="jobsFailed"
          width={0.15 * props.width}
          label="Failed"
          className="job-set-table-number-cell"
          cellRenderer={(cellProps) =>
            cellRendererForState(cellProps, props.onJobSetClick, "Failed")}/>
      </VirtualizedTable>
    </div>
  )
}